class Document < ApplicationRecord
  belongs_to :search, optional: true

  # Algoritmo de busca
  def self.search(search)
    Document.all
  end
end
