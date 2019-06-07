'use strict'

/** @type {typeof import('@adonisjs/lucid/src/Lucid/Model')} */
const Model = use("Model")

class Funder extends Model {
  projects() {
    return this.referOne('App/Models/Project', '_id', 'funder_id')
  }
}

module.exports = Funder
