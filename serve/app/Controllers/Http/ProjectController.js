'use strict'
const Project = use("App/Models/Project");

class ProjectController {
  async index() {
    let query = Project.query();

    return await query.paginate(1, 10);
  }

  async show({ params }) {
    return Project.find(params.id);
  }

  async count() {
    let query = Project.query();

    return {
      count: await this._countAll(query)
    }
  }

  async _countAll(query) {
    return await query.count()
  }

  async funders() {
    return await Project.query().sum('total')
  }

}

module.exports = ProjectController
