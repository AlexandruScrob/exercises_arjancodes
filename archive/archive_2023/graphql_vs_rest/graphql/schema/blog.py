from typing import List
from ariadne import ObjectType
from graphql import GraphQLResolveInfo
from schema.types import query, mutation
from data import Blog, all_blogs, get_blog, Author, BlogPayload, get_author, update_blog


BLOG_TYPEDEF = """
    type Blog {
        id: ID!
        title: String!
        content: String!
        author: Author!
    }
    
    input BlogPayload {
        title: String
        content: String
    }
    
    type Mutation {
        update_blog(id: ID!, payload: BlogPayload!): Blog
    }
"""


blog_query = ObjectType("Blog")


@query.field("blogs")
def resolve_blogs(_, info: GraphQLResolveInfo) -> List[Blog]:
    return all_blogs()


@query.field("blog")
def resolve_blog(_, info: GraphQLResolveInfo, blog_id: int) -> Blog:
    return get_blog(blog_id)


@mutation.field("update_blog")
def resolve_update_blog(
    _, info: GraphQLResolveInfo, blog_id: int, payload: BlogPayload
):
    return update_blog(int(id), payload)


@blog_query.field("author")
def resolve_author(blog, info: GraphQLResolveInfo) -> Author:
    return get_author(blog["author_id"])
