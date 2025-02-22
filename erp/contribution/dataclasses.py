from dataclasses import dataclass, field

from django.templatetags.static import static
from django.utils.safestring import mark_safe

UNIQUE_ANSWER = "unique"
MUTIPLE_ANSWERS = "multiple"
UNIQUE_OR_INT_ANSWER = "unique_or_int"
FREE_TEXT_ANSWER = "free_text"


@dataclass
class Question:
    label: str
    type: str
    answers: list
    display_conditions: list = field(default_factory=list)

    @property
    def choices(self):
        return [(a.label, mark_safe(f"{a.image_tag}{a.label}")) for a in self.answers]

    @property
    def is_unique_type(self):
        return self.type == UNIQUE_ANSWER

    @property
    def is_unique_or_int_type(self):
        return self.type == UNIQUE_OR_INT_ANSWER

    @property
    def is_mutiple_type(self):
        return self.type == MUTIPLE_ANSWERS

    @property
    def is_free_text_type(self):
        return self.type == FREE_TEXT_ANSWER

    @property
    def free_text_field(self):
        return "commentaire"


@dataclass
class Answer:
    label: str
    picture: str
    modelisations: list

    @property
    def image_tag(self):
        path = f"img/contrib_v2/{self.picture}"
        return f"<img src='{static(path)}' alt='{self.label}' class='w-100 h-auto'>"

    @property
    def safe_label(self):
        return self.label.replace("'", " ")
