from odoo import fields,api,models


class ProjectTicket(models.Model):
    _name = 'project.ticket'
    _inherits = {'project.task': 'task_id'}
    _description = 'Project Ticket'

    task_id = fields.Many2one(
        comodel_name='project.task',
        string='Task',
        required=True,
        ondelete='cascade',
    )

    actions_todo = fields.Html()

    def action_assign_to_me(self):
        self.ensure_one()
        return self.task_id.action_assign_to_me()
    
    def action_open_ratings(self):
        self.ensure_one()
        return self.task_id.action_open_ratings()

    def action_open_parent_task(self):
        self.ensure_one()
        return self.task_id.action_open_parent_task()
    
    def action_recurring_tasks(self):
        self.ensure_one()
        return self.task_id.action_recurring_tasks()

    def action_dependent_tasks(self):
        self.ensure_one()
        return self.task_id.action_dependent_tasks()