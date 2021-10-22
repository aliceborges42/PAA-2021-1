class Document < ApplicationRecord
  belongs_to :search, optional: true
end
