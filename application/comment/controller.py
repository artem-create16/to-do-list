from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user
from application import db
from application.models import User, Task, Project, Status, Comment, Species
from application.comment.form import CommentForm


def show_comments(task_id):
    task = Task.query.get(task_id)
    return render_template('comment/comment.html',
                           title='Comments', task=task,
                           comments=task.comments)


def create_comment(task_id, parent_id):
    task = Task.query.get(task_id)
    parent = Comment.query.get(parent_id)
    species = Species.to_the_comment.name
    if parent is None:
        parent = task
        species = Species.to_the_task.name
        parent_id = None
    form = CommentForm()
    if request.method == 'POST':
        print("000000000", flush=True)
        new_comment = Comment(
            subject=form.subject.data,
            creator_id=current_user.id,
            task_id=task.id,
            parent_id=parent_id,
            species=species
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('comment.show_comments', task_id=task_id))
    return render_template('comment/add_comment.html', parent=parent, task=task, form=form)
