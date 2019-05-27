'use strict'
const Project = use("App/Models/Project");

class ProjectController {
  async index() {
    let query = Project.query();

    return await query.paginate(1, 10);
  }

  async _countAll(query) {
    return await query.count()
  }

  async show({ request, params }) {
    return Project.find(params.id);
  }

  async count() {
    let query = Project.query();

    return {
      count: await this._countAll(query)
    }
  }
}

module.exports = ProjectController
