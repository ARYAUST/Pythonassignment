from playwright.sync_api import sync_playwright, expect

from playwright.sync_api import Page, expect

def test_login(page: Page) -> None:

    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("standard_user")

    page.locator('[data-test="password"]').fill("secret_sauce")

    page.locator('[data-test="login-button"]').click()

    expect(page).to_have_url("https://www.saucedemo.com/wrong-url.html")