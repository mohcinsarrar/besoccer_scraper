
<div id="top"></div>
<div align="center">
  <h1 align="center">Besoccer.com Scraper</h1>
</div>

Is a simple and functional solution to extract data from Besoccer.com. The program carefully processes the page for each date from the Besoccer website, saving the html content in your computer.
<br>This program built with the python library <a href="https://playwright.dev/">Playwright</a>.

![Logo_besoccer_th](https://github.com/mohcinsarrar/besoccer_scraper/assets/43006742/076b66a2-f767-428e-bdd6-1c0024f130c7)

scraping matchs from besoccer.com using python Playwright libray

<!-- GETTING STARTED -->
## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mohcinsarrar/besoccer_scraper.git
   ```
2. Install playwright
   ```sh
   pip install playwright
   ```
3. Set up the Playwright WebKit
  ```sh
   playwright install
   ```
  ```sh
   playwright install-deps
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage



```sh
   python scraper.py -s 'start date' -e 'end date'
```

you need to specify start ans end dates

the results will be stored to files named date.html in the current folder
