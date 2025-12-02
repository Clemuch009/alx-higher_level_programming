from ariadne import gql, load_schema_from_path

schema = load_schema_from_path("schema.graphql")

schema = load_schema_from_path("schema")

schema = gql("""
             type Query {
             user: User
             }
             type User {
             id: ID
             username: String!
             }
             """
             )
