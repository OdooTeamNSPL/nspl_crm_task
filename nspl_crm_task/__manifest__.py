{
    "name": " Generate Task from Lead",
    "version": "17.0",
    'summary': """This module helps user to easily create new task with deadline and project name directly from lead.""",
    'description': """
Task on Lead, Add Task from Lead, Lead Tasks, Create Project Task from Lead, Task from Email, Create Task from Mail — all made easy with this module.

✔ Automatically create project tasks from CRM leads or incoming emails.
✔ Sync essential lead details (e.g., name, description, contact info) directly to the generated task.
✔ Configure rules to control when and how tasks are created from leads.
✔ Link tasks to leads for better traceability between sales and project teams.
✔ Improve coordination by managing lead-related tasks within the Project module.

Ideal for sales teams, project managers, and CRM users who want to bridge the gap between lead management and task execution.

    """,
    'category': 'Project',
    'sequence': 2,
    'author': 'Namah Softech Private Limited',
    'website': 'http://namahsoftech.com/',
    'license': 'OPL-1',
    'price': 9.99,
    'currency': 'USD',
    'support': 'support@namahsoftech.com',
    'contributors': ["Rutik Patil"],
    'depends': ['base', 'crm', 'sale', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_view.xml'
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,

}
