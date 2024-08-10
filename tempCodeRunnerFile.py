@app.route('/admin/dashboard/get_project/<int:project_id>', methods=['GET'])
# def get_project(project_id):
#     project = ProjectData.query.get_or_404(project_id)
#     return render_template('admin_dashboard.html', project=project)