from wechat.page.admin_address_page import AdminAddressPage


class TestAddMember:
    def setup(self):
        self.home = AdminAddressPage(reuse=True)

    def test_edit_user(self):
        self.home.edit_user("hhhh")