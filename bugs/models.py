from distutils.command.upload import upload
from random import choices
from sqlite3 import Date
from tabnanny import verbose
from xmlrpc.client import DateTime
from django.db import models
from project.models import Project
from userprofile.models import Profile
import uuid
from constants.constants import BUG_STATUS, DEVELOPER, QAENGINEER, BUG_TYPE, NEW
from django.urls import reverse


class Bug(models.Model):
  id = models.UUIDField(verbose_name="Bug ID", primary_key=True, default = uuid.uuid4, editable = False)
  project = models.ForeignKey(Project, blank=False, null=False, verbose_name="Found In Project", on_delete=models.CASCADE)
  title = models.CharField(max_length=100, verbose_name="Bug Title", null=False, blank=False)
  description = models.TextField(max_length=500, verbose_name="Describe bug/feature in a paragraph", blank=True, null=True)
  deadline = models.DateField(verbose_name="Bug Deadline", auto_now_add=True, blank=True)
  type = models.CharField(max_length=20,verbose_name="Is it a Feature or Bug", choices=BUG_TYPE, null=False, blank=False, default=BUG_TYPE[0][0])
  status = models.CharField(max_length=20,verbose_name="Bug/Feature Status", choices=BUG_STATUS, null=False, blank=False, default=NEW)
  creator = models.ForeignKey(Profile, verbose_name="Creator of Bug/Feature", null=False, blank=False, limit_choices_to={'designation': QAENGINEER}, on_delete=models.PROTECT, related_name="creator_qae")
  assigned_to = models.ForeignKey(Profile, verbose_name="Developer Assigned To", on_delete=models.DO_NOTHING, blank=True, null=True, limit_choices_to={'designation': DEVELOPER}, related_name="developer_assigned")
  screenshot = models.ImageField(upload_to='bugs_imgs')

  def __str__(self):
    return self.title

  def get_absolute_url(self):
      return reverse('bug-view', kwargs={"pk": self.pk})

