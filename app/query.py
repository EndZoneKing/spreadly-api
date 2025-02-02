import graphene
from app.queries.message import Message
from app.queries.user import User
from app import asgi

class Query(graphene.ObjectType):
    """Root GraphQL query."""

    history = graphene.List(Message, chatroom=graphene.String())
    user = graphene.Field(User)

    def resolve_history(self, info, chatroom):
        """Return chat history."""
        del info
        return asgi.chats[chatroom] if chatroom in asgi.chats else []

    def resolve_user(self, info):
        """Provide currently logged in user."""
        if info.context.user.is_authenticated:
            return info.context.user
        return None