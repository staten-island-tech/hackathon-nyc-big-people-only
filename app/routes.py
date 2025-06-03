from flask import render_template, request, redirect, url_for, flash
from . import db
from .models import Toilet, Review, PoopStory
from .forms import ToiletForm, ReviewForm, PoopStoryForm
from flask import current_app as app

@app.route('/')
def home():
    toilets = Toilet.query.all()
    story = PoopStory.query.order_by(PoopStory.upvotes.desc()).first()
    return render_template('home.html', toilets=toilets, story=story)

@app.route('/toilet/<int:toilet_id>', methods=['GET', 'POST'])
def toilet_detail(toilet_id):
    toilet = Toilet.query.get_or_404(toilet_id)
    form = ReviewForm()
    if form.validate_on_submit():
        review = Review(
            toilet_id=toilet.id,
            cleanliness=form.cleanliness.data,
            safety=form.safety.data,
            smell=form.smell.data,
            comment=form.comment.data
        )
        db.session.add(review)
        db.session.commit()
        flash('Review submitted!')
        return redirect(url_for('toilet_detail', toilet_id=toilet_id))
    return render_template('toilet_detail.html', toilet=toilet, form=form)

@app.route('/submit', methods=['GET', 'POST'])
def submit_toilet():
    form = ToiletForm()
    if form.validate_on_submit():
        toilet = Toilet(
            name=form.name.data,
            location=form.location.data,
            lat=form.lat.data,
            lon=form.lon.data
        )
        db.session.add(toilet)
        db.session.commit()
        flash('Toilet added!')
        return redirect(url_for('home'))
    return render_template('submit_toilet.html', form=form)

@app.route('/poop-story', methods=['GET', 'POST'])
def poop_story():
    form = PoopStoryForm()
    if form.validate_on_submit():
        story = PoopStory(
            title=form.title.data,
            content=form.content.data
        )
        db.session.add(story)
        db.session.commit()
        flash('Story shared!')
        return redirect(url_for('home'))
    return render_template('poop_story.html', form=form)
