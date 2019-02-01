from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields import TextAreaField
from wtforms.validators import DataRequired, length

class SimilarityForm(FlaskForm):
    text1 = TextAreaField('First Text', validators=[DataRequired(), length(max=200)], render_kw={'class': 'form-control', 'rows': 5, 'cols': 50})
    text2 = TextAreaField('Second Text', validators=[DataRequired(), length(max=200)], render_kw={'class': 'form-control', 'rows': 5, 'cols': 50})
    submit = SubmitField('Calculate similarity', render_kw={'class': 'btn'})


class SimilarityFormPaste(FlaskForm):
    text_box = TextAreaField('Text', validators=[DataRequired(), length(max=10000)], render_kw={'class': 'form-control', 'rows': 20, 'cols': 100})
    submit = SubmitField('Calculate similarity', render_kw={'class': 'btn'})
