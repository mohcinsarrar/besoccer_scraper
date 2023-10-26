from playwright.async_api import async_playwright
from datetime import datetime, timedelta
import asyncio
import argparse
import sys

parser = argparse.ArgumentParser(description="This python script used to extract data from besoccer.com. developed by : Mohcin S. https://www.upwork.com/freelancers/~01901f654ceb7c53fc ")
parser.add_argument('-s', '--start', required=True, help="The start date")
parser.add_argument('-e', '--end', required=True, help="The end date")
args = parser.parse_args()
start = args.start
end = args.end

def generate_date(start,end):
    start_date = datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.strptime(end, '%Y-%m-%d')
    
    if start_date>end_date:
        print('start date must be less or equal to end date')
        sys.exit()
    today = datetime.now()
    if end_date <= today:
        date_list = []
        while start_date <= end_date:
            date_list.append(start_date.strftime('%Y-%m-%d'))
            start_date += timedelta(days=1)

        return date_list
    else:
        print('end date must be less or equal to today date')
        sys.exit()


async def get_page_post(date):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.goto(f"https://www.besoccer.com/livescore/{date}")

        previous_height = 0
        current_height = 1

        # Scroll until all data is loaded (you can change the condition as needed)
        while previous_height != current_height:
            previous_height = current_height
            # Scroll down the page by a specific amount (you can change this)
            await page.evaluate('window.scrollBy(0, 500)')  # Scroll down by 500 pixels
            # Wait for some time to allow new content to load (you can adjust the timing)
            await page.wait_for_timeout(1000)  # Wait for 1 second

            # Get the current scroll position
            current_height = await page.evaluate('window.scrollY')

        html_content = await page.content()

        await browser.close()

    return html_content


dates = generate_date(start,end)
for date in dates:
    result = asyncio.run(get_page_post(date))
    text_file = open(f"./{date}.html", "w")
    text_file.write(result)
    text_file.close()
    print(f"file stored for date {date}")
