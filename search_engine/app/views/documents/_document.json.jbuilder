json.extract! document, :id, :url, :title, :body, :created_at, :updated_at
json.url document_url(document, format: :json)
