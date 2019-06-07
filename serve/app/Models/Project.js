'use strict'

/** @type {typeof import('@adonisjs/lucid/src/Lucid/Model')} */
const Model = use('Model')

class Project extends Model {
  funders() {
    return this.embedsMany("App/Models/Funder", "_id", "funder_id")
  }
}

module.exports = Project
