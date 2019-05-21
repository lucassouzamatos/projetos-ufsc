'use strict'

class ProjectController {
  async index({ response }) {
    return response.send('projects')
  }
}

module.exports = ProjectController
