from wechat.page.admin_home_page import AdminHomePage


class TestAdminHome:
    def setup(self):
        self.home = AdminHomePage(reuse=True)

    def test_goto_addmember(self):
        result = self.home.goto_add_member()
        assert "添加成员" in result

    def test_import_user(self):
        # import_user()
        # assert xx in import_user()
        pass

    def test_send_message(self):
        # send.message()
        # assert xx in get_message()
        pass
