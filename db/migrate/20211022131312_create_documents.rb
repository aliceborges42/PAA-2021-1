class CreateDocuments < ActiveRecord::Migration[6.0]
  def change
    create_table :documents do |t|
      t.string :url
      t.string :title
      t.text :body

      t.timestamps
    end
  end
end
