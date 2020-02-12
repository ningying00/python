from wechat.page.admin_address_page import AdminAddressPage


class TestAddMember:
    def setup(self):
        self.home = AdminAddressPage(reuse=True)

    # 正向case，添加成员
    def test_add(self, username=1, account=5, phone=18532687062):
        result = self.home.add_member(username + 1, account + 1, phone + 1)
        assert "保存成功" in result[1]

    def test_username_phone(self):
        result = self.home.add_member(username="abc", account=11111, phone=18582687018)
        assert "占有" in result
    def test_join_member(self):
        pass

