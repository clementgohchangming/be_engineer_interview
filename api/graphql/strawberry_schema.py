import strawberry

@strawberry.type
class Query:
    @strawberry.field
    def get_lead_information(self) -> str:
        return "Hello, world!"
    
@strawberry.type
class Mutation:
    @strawberry.mutation
    def hello(self) -> str:
        return "Hello, world!"