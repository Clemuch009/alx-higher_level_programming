from flask import Flask, request, jsonify
from ariadne import QueryType, make_executable_schema, graphql_sync
from ariadne.explorer import ExplorerGraphiQL


type_defs = """
type Query {
hello: String!
}
"""

query = QueryType()

@query.field("hello")
def resolve_hello(_, info):
    return "Hello Muchai! GraphQL with Ariadne + Flask."

schema =make_executable_schema(type_defs, query)

app = Flask(__name__)
explorer_html = ExplorerGraphiQL().html({})


@app.route("/graphql", methods=["GET"])
def graphql_explorer():
    return explorer_html, 200

@app.route('/graphql', methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
            schema,
            data,
            context_value=request,
            )
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(debug=True)
