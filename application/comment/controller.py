from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user
from application import db
from application.models import User, Task, Project, Status, Comment
from application.comment.form import CommentForm


def show_comments(task_id):
    task = Task.query.get(task_id)
    form = CommentForm()
    if request.method == 'POST':
        new_comment = Comment(
            body=form.body.data,
            author_id=current_user.id,
            task_id=task.id
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('comment.show_comments', task_id=task_id))
    return render_template('comment/comment.html',
                           title='Creating task',
                           form=form, task=task,
                           comments=task.comments)