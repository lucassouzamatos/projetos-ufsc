'use strict'

/** @typedef {import('@adonisjs/framework/src/Request')} Request */
/** @typedef {import('@adonisjs/framework/src/Response')} Response */
/** @typedef {import('@adonisjs/framework/src/View')} View */

const Funder = use("App/Models/Funder");

/**
 * Resourceful controller for interacting with funders
 */
class FunderController {
  /**
   * Show a list of all funders.
   * GET funders
   *
   * @param {object} ctx
   * @param {Request} ctx.request
   * @param {Response} ctx.response
   * @param {View} ctx.view
   */
  async index ({ request, response, view }) {
    return Funder
      .query()
      .with("projects")
      .fetch();
  }

  async count() {
    return Funder
      .query()
      .withCount(builder => {

      });
  }
}

module.exports = FunderController
