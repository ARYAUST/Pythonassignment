from playwright.sync_api import Page, expect

def test_orangehrm_login(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")

    page.get_by_role("button", name="Login").click()
    expect (page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")



def test_radio_buttons(page):

    #Step 1: Open radio button URL

    page.goto("https://practice.expandtesting.com/radio-buttons")

    #Step 2: Locate Radio buttons using their labels

    blue_radio = page.get_by_label("Blue")

    red_radio = page.get_by_label("Red")

    yellow_radio = page.get_by_label("Yellow")

    #Step 3: Select Blue radio button

    blue_radio.check()

    #Step 4: Verify the Blue is selected

    expect(blue_radio).to_be_checked()

    #Step 5: Select Blue radio button

    red_radio.check()

    #Step 6: Verify the Red is selected

    expect(red_radio).to_be_checked()

    #Step 7: Select Yellow radio button

    yellow_radio.check()

    #Step 8: Verify the Yellow is selected

    expect(yellow_radio).to_be_checked()

    #Step 9: Verify that Blue is no longer selected

    expect(blue_radio).not_to_be_checked()

    #Step 10: Verify that Red is no longer selected

    expect(red_radio).not_to_be_checked()

    print("Radio button selection tests passed.")




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

    #step 5 Interact with the second tab
    expect (second_page.get_by_role("heading", name="Wikipedia").to_be_visible())

    #step 6: close the second tab
    second_page.close()

    #step 7: verify the original tab remains open
    expect(page).to_have_title("Example Domain")

    assert len(page.context.pages)==1
    print("Multiple tabs test passed successfully")
            