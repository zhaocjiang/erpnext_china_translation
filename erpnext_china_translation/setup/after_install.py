# ERPNext中国汉化翻译模块 - workspace特殊翻译功能

import json
import os
from pathlib import Path
import warnings

import frappe


def overwrite_workspace():
    """覆盖workspace文件，汉化特殊位置如Your Shortcuts、Reports & Masters等"""
    # 获取bench根目录
    bench_path = Path(__file__).parent.parent.parent.parent.parent
    
    # 定义workspace文件路径
    workspace_file_path = [
        # Frappe workspaces
        (bench_path / 'apps' / 'frappe' / 'frappe' / 'automation' / 'workspace'  / 'tools' / 'tools.json'),
        (bench_path / 'apps' / 'frappe' / 'frappe' / 'website' / 'workspace'  / 'website' / 'website.json'),
        (bench_path / 'apps' / 'frappe' / 'frappe' / 'core' / 'workspace'  / 'build' / 'build.json'),
        (bench_path / 'apps' / 'frappe' / 'frappe' / 'integrations' / 'workspace'  / 'integrations' / 'integrations.json'),
        
        # ERPNext workspaces
        (bench_path / 'apps' / 'erpnext' / 'erpnext' / 'setup' / 'workspace'  / 'home' / 'home.json'),
        (bench_path / 'apps' / 'erpnext' / 'erpnext' / 'accounts' / 'workspace'  / 'accounting' / 'accounting.json'),
        (bench_path / 'apps' / 'erpnext' / 'erpnext' / 'assets' / 'workspace'  / 'assets' / 'assets.json'),
        (bench_path / 'apps' / 'erpnext' / 'erpnext' / 'quality_management' / 'workspace'  / 'quality' / 'quality.json'),
        (bench_path / 'apps' / 'erpnext' / 'erpnext' / 'projects' / 'workspace'  / 'projects' / 'projects.json'),
        (bench_path / 'apps' / 'erpnext' / 'erpnext' / 'support' / 'workspace'  / 'support' / 'support.json'),
        (bench_path / 'apps' / 'erpnext' / 'erpnext' / 'setup' / 'workspace'  / 'erpnext_settings' / 'erpnext_settings.json'),
        (bench_path / 'apps' / 'erpnext' / 'erpnext' / 'erpnext_integrations' / 'workspace'  / 'erpnext_integrations' / 'erpnext_integrations.json'),
        (bench_path / 'apps' / 'erpnext' / 'erpnext' / 'crm' / 'workspace' / 'crm' / 'crm.json'),
        (bench_path / 'apps' / 'erpnext' / 'erpnext' / 'buying' / 'workspace' / 'buying' / 'buying.json'),
        (bench_path / 'apps' / 'erpnext' / 'erpnext' / 'manufacturing' / 'workspace' / 'manufacturing' / 'manufacturing.json'),
        (bench_path / 'apps' / 'erpnext' / 'erpnext' / 'selling' / 'workspace' / 'selling' / 'selling.json'),
        (bench_path / 'apps' / 'erpnext' / 'erpnext' / 'stock' / 'workspace' / 'stock' / 'stock.json'),
    ]
    
    for file_path in workspace_file_path:
        # 检查文件是否存在
        if file_path.exists():
            save_workspace_blocks(file_path)


def save_workspace_blocks(file_path):
    """修改workspace文件中的英文标题为中文"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        
        # 替换英文标题为中文
        updated_content = file_content \
            .replace('<b>Your Shortcuts</b>', '<b>快捷入口</b>') \
            .replace('<b>Reports &amp; Masters</b>', '<b>功能&报表</b>') \
            .replace('<b>Quick Access</b>', '<b>快捷入口</b>') \
            .replace('<b>Masters & Reports</b>', '<b>功能&报表</b>')
        
        # 使修改后的workspace生效
        data = json.loads(updated_content)
        args = {
            "title": data['title'],
            "public": data['public'],
            "new_widgets": json.dumps({}),
            "blocks": data['content']
        }
        
        try:
            frappe.call("frappe.desk.doctype.workspace.workspace.save_page", **args)
        except frappe.exceptions.LinkValidationError as e:
            # 捕获LinkValidationError错误并将其转换为警告
            warning_message = str(e)
            warnings.warn(warning_message, Warning)
            
    except Exception as e:
        # 记录其他错误但继续处理下一个文件
        frappe.log_error(message=str(e), title=f"Failed to update workspace: {file_path}")