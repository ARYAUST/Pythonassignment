from playwright .sync_api import expect
def test_dynamic_loading (page):
    page.goto("https://the-internet.herokuapp.com/");
    page.get_by_role("button", name="Start").click()
    heading=page.locator("#finish h4")
    heading.wait_for(
        state="visible"
        timeout=10000
    )
    expect(heading).to_have_text("Hello World!")

    
    