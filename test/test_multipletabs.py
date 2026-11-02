from playwright.sync_api import Page, expect

def test_multiple_tabs(page: Page):

    #step 1: open first website

    page.goto("https://example.com")

    #Verify the first webpage

    expect(page).to_have_title("Example Domain")

    print("First tab URL: ", page.url)

    #Step 2: Create a second tab in same browser

    second_page = page.context.new_page()

    second_page.goto("https://www.wikipedia.org")

    #Verify the second website

    expect(second_page).to_have_title("Wikipedia")

    print("Second tab URL:", second_page.url)

    #Step 3: Verify the original tab is still open

    expect(page).to_have_title("Example Domain")

    #Step 4: Verify that two pages exist in the context

    all_pages = page.context.pages

    assert len(all_pages) == 2

    print("No.of open pages:", len(all_pages))