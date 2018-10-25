# fun fact – this file can't be named `graphql.py`
# https://github.com/graphql-python/graphene/issues/441
import graphene

class Post(graphene.ObjectType):
  title = graphene.String()
  text = graphene.String()

  def resolve_title(self, info):
    return self.title

  def resolve_text(self, info):
    return self.text

class Person(graphene.ObjectType):
  name = graphene.String()
  age = graphene.Int()
  posts = graphene.List(Post, default_value=[])

  def resolve_name(self, info):
    return self.name

  def resolve_age(self, info):
    return self.age

  def resolve_posts(self, info):
    result = []
    for postID in self.posts:
      if postID == 'first_post':
        result.append(first_post)

    return result


first_post = Post(title = 'first_post', text="sdsa")
seva = Person(name="Seva", age=27, posts = ['first_post'])
jess = Person(name="Jess", age=29)

class Query(graphene.ObjectType):
  hello = graphene.String(name = graphene.String(default_value="some value"))
  person = graphene.Field(Person, name = graphene.String(default_value="Seva"))
  all_persons = graphene.List(Person)

  def resolve_hello(self, info, name):
    return "hello, " + name

  def resolve_person(self, info, name):
    if name == "Seva":
      return seva

    return jess

  def resolve_all_persons(self, info):
    return [seva, jess]

schema = graphene.Schema(query=Query)

hello_query = '''
    query SayHello($name: String!) {
      hello(name: $name)
    }
'''

person_query = '''
  query getPerson($name: String!) {
    person(name: $name) {
      name,
      age
    }
  }
'''

query = '''
  query getAllPersdssdgdfsgfdsons {
    allPersons {
      name,
      age,
      posts {
        title
      }
    }
  }
'''
result = schema.execute(query)

print(result.data)