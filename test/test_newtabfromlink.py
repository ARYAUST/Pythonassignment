from pathlib import Path
from playwright.sync_api import expect
def test_new_tabfrom_link(page):
    # step1: open the HTML page
    html_file = Path(__file__).with_name("open_new_tab.html")

    page.goto(html_file.resolve().as_uri)
    expect(page.get_by_role("heading", name="original Page")).to_be_visible()

    with page.context.expect.page() as new_page_info:
        page.get_by_role(
            "link",
            name= " open Example website in a new tab").click()
        #step 4:Capture the newly opened tab

        new_page = new_page_info.value

       # verify the new page
    expect(new_page).to_have_url("https://example.com/")
    expect(new_page.get_by_role("heading", name = "Example Domain")).to_be_visible()

    # verify the original page remains open
    expect(page.get_by_role("heading", name= "Original Page")).to_be_visible()

    # step 7 close the new tab
    new_page.close()
    print("New Tab Test passed succesfully")

    

