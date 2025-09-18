app_name = "erpnext_china_translation"
app_title = "ERPNext China Translation"
app_publisher = "Translation Module"
app_description = "ERPNext中国汉化翻译模块 - 仅包含翻译功能"
app_email = ""
app_license = "mit"
app_logo_url = "/assets/erpnext/images/erpnext-logo.svg"

# 安装后执行的函数，用于处理workspace特殊翻译
after_install = "erpnext_china_translation.setup.after_install.overwrite_workspace"

# 不需要其他功能的配置