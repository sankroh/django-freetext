from django.db import models
from django.utils.translation import ugettext_lazy as _

class FreeText(models.Model):
    """
    A piece of content associated with a unique slug that can be inserted 
    into any template with the use of a special template tag.
    
    """
    title = models.CharField(_("title"), max_length=255,
                help_text=_("Title for this content, for your reference."))
    slug = models.SlugField(max_length=255, unique=True,
                help_text=_("A unique name used for reference in the templates (auto-generated!)."))
    header = models.CharField(blank=True, null=True, max_length=255,
                help_text=_("An optional header for this content."))
    content = models.TextField(blank=True, null=True)
    active = models.BooleanField(_("active"), default=False)

    class Meta:
        verbose_name = 'free text'
        verbose_name_plural = 'free text'

    def __unicode__(self):
        return u"%s" % (self.title,)

