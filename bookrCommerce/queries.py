# queries used for unit testing and for graphQL testing

PRODUCTS_QUERY = """query {
    products {
        id
        name
        description
        price
    }
}"""


# PRODUCTS_QUERY_NAME = """query{
#     productByName(name: "Head and shoulder"){
#         id
#         name
#         description
#         price
#     }
# }"""

PRODUCTS_QUERY_NAME = """query($name: String!) {
   productByName(name: $name) {
    id
    name
    description
    price
  }
}"""

# Create product
# CREATE_PRODUCT_QUERY = """mutation {
#     create_product:createProduct(input: {name:"Choclate", price: "10.1", description: "123"}) {
#          product{
#          name
#          price
#          description
#        }
#      }
#    }
# """

CREATE_PRODUCT_QUERY = """mutation CreateProduct($input: ProductInput!){
    create_product:createProduct(input: $input) {
         product{
         name
         price
         description
       }
     }
   }
"""

UPDATE_PRODUCT_QUERY = """mutation UpdateProduct($id: ID!, $input: ProductInput!){
update_product:updateProduct(id: $id, input: $input) {
        product{
        name
        price
        description
    }
    }
}"""
# update_product
# UPDATE_PRODUCT_QUERY = """mutation {
# update_product:updateProduct(id: 1, input: {name:"asdasdadasdasd", price: "10.1", description: "123"}) {
#         product{
#         name
#         price
#         description
#     }
#     }
# }"""
