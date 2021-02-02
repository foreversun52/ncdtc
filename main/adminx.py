import xadmin
from main import models

# 自定义xadmin主题
from xadmin import views
class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "哈尔滨医科大学网站管理后台"  # 设置站点标题
    site_footer = "哈尔滨医科大学"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠
xadmin.site.register(views.CommAdminView, GlobalSettings)
# Register your models here.
xadmin.site.register(models.NoncoRNA)
xadmin.site.register(models.Submit)
