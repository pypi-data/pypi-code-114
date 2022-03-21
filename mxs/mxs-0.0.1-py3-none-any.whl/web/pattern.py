"""
MXS is the Math eXploration Solver.
Copyright (C) 2022  Brian Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com
"""

from flask import (
    Blueprint, redirect, render_template, request, url_for, session
)

from mxs import api

bp = Blueprint('pattern', __name__, url_prefix='/pattern')


@bp.route('/answer')
def answer():
    return render_template('pattern/answer.html')


@bp.route('/pv', methods=('GET', 'POST'))
def reveal_position_value():
    if request.method == 'POST':
        pattern = request.form['pattern']
        char_per_line = request.form['char_per_line']
        target_line = request.form['target_line']
        target_char = request.form['target_char']

        target_position, value = api.reveal_position_value(
            pattern,
            char_per_line,
            target_line,
            target_char
        )

        session['answer'] = [
            {'label': 'Target Position', 'value': target_position},
            {'label': 'Value', 'value': value}
        ]

        return redirect(url_for('pattern.answer'))

    return render_template('pattern/pv.html')
