import requests
from bs4 import BeautifulSoup

def extract_features_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example feature extraction logic
        length_url = len(url)
        length_hostname = len(requests.utils.urlparse(url).hostname)
        ip = 1 if any(char.isdigit() for char in requests.utils.urlparse(url).hostname) else 0
        nb_dots = url.count('.')
        nb_hyphens = url.count('-')
        nb_at = url.count('@')
        nb_qm = url.count('?')
        nb_and = url.count('&')
        nb_eq = url.count('=')
        nb_slash = url.count('/')
        nb_semicolumn = url.count(';')
        nb_www = url.count('www')
        nb_com = url.count('.com')
        https_token = 1 if 'https' in url else 0
        ratio_digits_url = sum(c.isdigit() for c in url) / len(url)
        ratio_digits_host = sum(c.isdigit() for c in requests.utils.urlparse(url).hostname) / len(requests.utils.urlparse(url).hostname)
        tld_in_subdomain = 1 if requests.utils.urlparse(url).hostname.split('.')[-2] == 'com' else 0
        abnormal_subdomain = 1 if len(requests.utils.urlparse(url).hostname.split('.')) > 2 else 0
        nb_subdomains = len(requests.utils.urlparse(url).hostname.split('.'))
        prefix_suffix = 1 if '-' in requests.utils.urlparse(url).hostname else 0
        shortening_service = 1 if len(url) < 20 else 0
        length_words_raw = len(url.split('/'))
        shortest_word_host = min(len(word) for word in requests.utils.urlparse(url).hostname.split('.'))
        longest_words_raw = max(len(word) for word in url.split('/'))
        longest_word_host = max(len(word) for word in requests.utils.urlparse(url).hostname.split('.'))
        longest_word_path = max(len(word) for word in requests.utils.urlparse(url).path.split('/'))
        avg_words_raw = sum(len(word) for word in url.split('/')) / len(url.split('/'))
        avg_word_host = sum(len(word) for word in requests.utils.urlparse(url).hostname.split('.')) / len(requests.utils.urlparse(url).hostname.split('.'))
        avg_word_path = sum(len(word) for word in requests.utils.urlparse(url).path.split('/')) / len(requests.utils.urlparse(url).path.split('/'))
        phish_hints = url.lower().count('phish')
        suspecious_tld = 1 if requests.utils.urlparse(url).hostname.split('.')[-1] in ['tk', 'ml', 'ga', 'cf', 'gq'] else 0
        statistical_report = 0
        nb_hyperlinks = len(soup.find_all('a'))
        ratio_intHyperlinks = len([a for a in soup.find_all('a') if requests.utils.urlparse(a.get('href')).hostname == requests.utils.urlparse(url).hostname]) / len(soup.find_all('a')) if len(soup.find_all('a')) > 0 else 0
        ratio_extRedirection = len([a for a in soup.find_all('a') if a.get('href') and 'http' in a.get('href')]) / len(soup.find_all('a')) if len(soup.find_all('a')) > 0 else 0
        external_favicon = 1 if soup.find('link', rel='shortcut icon') and 'http' in soup.find('link', rel='shortcut icon').get('href') else 0
        links_in_tags = len(soup.find_all('link'))
        ratio_intMedia = len([img for img in soup.find_all('img') if requests.utils.urlparse(img.get('src')).hostname == requests.utils.urlparse(url).hostname]) / len(soup.find_all('img')) if len(soup.find_all('img')) > 0 else 0
        ratio_extMedia = len([img for img in soup.find_all('img') if img.get('src') and 'http' in img.get('src')]) / len(soup.find_all('img')) if len(soup.find_all('img')) > 0 else 0
        safe_anchor = len([a for a in soup.find_all('a') if not a.get('href') or '#' in a.get('href')]) / len(soup.find_all('a')) if len(soup.find_all('a')) > 0 else 0
        empty_title = 1 if not soup.title or not soup.title.string.strip() else 0
        domain_in_title = 1 if soup.title and requests.utils.urlparse(url).hostname in soup.title.string else 0
        domain_with_copyright = 1 if soup.find(text=lambda text: text and '©' in text) else 0
        domain_registration_length = 227  # This requires WHOIS lookup
        domain_age = -1  # This requires WHOIS lookup
        dns_record = 0 # This requires DNS lookup
        google_index = 1 # This requires Google search API
        page_rank = 2  # This requires external API
        
        # Example of features dictionary
        features1 = {
            'length_url': length_url,
            'length_hostname': length_hostname,
            'ip': ip,
            'nb_dots': nb_dots,
            'nb_hyphens': nb_hyphens,
            'nb_at': nb_at,
            'nb_qm': nb_qm,
            'nb_and': nb_and,
            'nb_eq': nb_eq,
            'nb_slash': nb_slash,
            'nb_semicolumn': nb_semicolumn,
            'nb_www': nb_www,
            'nb_com': nb_com,
            'https_token': https_token,
            'ratio_digits_url': ratio_digits_url,
            'ratio_digits_host': ratio_digits_host,
            'tld_in_subdomain': tld_in_subdomain,
            'abnormal_subdomain': abnormal_subdomain,
            'nb_subdomains': nb_subdomains,
            'prefix_suffix': prefix_suffix,
            'shortening_service': shortening_service,
            'length_words_raw': length_words_raw,
            'shortest_word_host': shortest_word_host,
            'longest_words_raw': longest_words_raw,
            'longest_word_host': longest_word_host,
            'longest_word_path': longest_word_path,
            'avg_words_raw': avg_words_raw,
            'avg_word_host': avg_word_host,
            'avg_word_path': avg_word_path,
            'phish_hints': phish_hints,
            'suspecious_tld': suspecious_tld,
            'statistical_report': statistical_report,
            'nb_hyperlinks': nb_hyperlinks,
            'ratio_intHyperlinks': ratio_intHyperlinks,
            'ratio_extRedirection': ratio_extRedirection,
            'external_favicon': external_favicon,
            'links_in_tags': links_in_tags,
            'ratio_intMedia': ratio_intMedia,
            'ratio_extMedia': ratio_extMedia,
            'safe_anchor': safe_anchor,
            'empty_title': empty_title,
            'domain_in_title': domain_in_title,
            'domain_with_copyright': domain_with_copyright,
            'domain_registration_length': domain_registration_length,
            'domain_age': domain_age,
            'dns_record': dns_record,
            'google_index': google_index,
            'page_rank': page_rank
        }

        features = {
            'length_url': length_url,
            'length_hostname': length_hostname,
            'ip': ip,
            'nb_dots': nb_dots,
            'nb_qm': nb_qm,
            'nb_eq': nb_eq,
            'nb_slash': nb_slash,
            'nb_www': nb_www,
            'ratio_digits_url': ratio_digits_url,
            'ratio_digits_host': ratio_digits_host,
            'tld_in_subdomain': tld_in_subdomain,
            'prefix_suffix': prefix_suffix,
            
            'shortest_word_host': shortest_word_host,
            'longest_words_raw': longest_words_raw,
            
            'longest_word_path': longest_word_path,
            
            'phish_hints': phish_hints,
            
            'nb_hyperlinks': nb_hyperlinks,
            'ratio_intHyperlinks': ratio_intHyperlinks,
            
            'empty_title': empty_title,
            'domain_in_title': domain_in_title
            
        }
        print(features1)
        return features
    except Exception as e:
        print(f"Error extracting features from URL: {e}")
        return {}
