from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # lauch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo = 3000) #1s = 1000 milliseconds, headless=True : chạy ẩn
    # create a new tab
    page = browser.new_page()

    # navigate to "https://www.planz.ai"
    page.goto("https://www.planz.ai")

    print("Link của trang chủ Planz là:", page.url)

    doc_link = page.get_by_role("link", name="ĐĂNG NHẬP") #định vị thẻ
    with page.expect_popup() as popup_info: #Bắt event "popup" khi mở tab mới
        doc_link.click() # <- phải thụt vào đây

    new_page = popup_info.value
    new_page.wait_for_load_state()

    print("Link của trang Đăng Nhập là: ", new_page.url)
    page.close()

