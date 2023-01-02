import requests
from bs4 import BeautifulSoup

html = '''
<div class="columns small-12">
      <table class="domain-record-table">
        <thead>
          <tr>
            <th class="type">Type</th>
            <th class="hostNames">Hostname</th>
            <th class="value">Value</th>
            <th class="ttl">TTL (seconds)</th>
            <th class="action"></th>
          </tr>
        </thead>
        <tbody>
              <tr id="ember2773" class="a ember-view">  <td class="type">
    A
  </td>
  <td class="hostNames">
    <div class="click-to-copy-wrap">
      <div id="ember2774" class="click-to-copy ember-view">    <span class="click-to-copy-text">webmin.asurraa.dev</span>

    <span data-label="Copied" class="Label click-to-copy-label hidden">Copy</span>
<!----></div>
    </div>
  </td>
  <td class="value editable">
      <span class="domainRow--prefix">directs to</span>
      <div class="click-to-copy-wrap">
        <div id="ember2775" class="click-to-copy ember-view">    <span class="click-to-copy-text">109.123.236.46</span>

    <span data-label="Copied" class="Label click-to-copy-label hidden">Copy</span>
<!----></div>
      </div>
<!---->  </td>
  <td class="ttl editable">
      <div id="ember2776" class="click-to-copy ember-view">    <span class="click-to-copy-text">3600</span>

    <span data-label="Copied" class="Label hidden click-to-copy-label">Copy</span>
<!----></div> 
'''
# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extract the text content of the element
hostname = soup.select_one('.hostNames .click-to-copy-text').text


# Extract the text content of the element
value = soup.select_one('.value .click-to-copy-text').text


# Extract the text content of the element
ttl  = soup.select_one('.ttl .click-to-copy-text').text

# Print the hostname, value, and ttl
print(f'Hostname: {hostname}')
print(f'Value: {value}')
print(f'TTL: {ttl}')


import pandas as pd

# Create a dataframe with the scraped data
df = pd.DataFrame({'Hostname': [hostname],'Value': [value], 'TTL': [ttl]})

# Write the dataframe to an Excel file
df.to_excel('D:\scraped_data.xlsx', index=False)
existing_df = pd.read_excel('D:\scraped_data.xlsx')
