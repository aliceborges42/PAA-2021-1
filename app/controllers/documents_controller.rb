class DocumentsController < ApplicationController
  before_action :set_document, only: %i[ show edit update destroy ]

  # GET /documents or /documents.json
  def index
		user_input = params[:q]
		puts "USER INPUT"
		puts user_input
		terms = user_input.split(/(.+?)((?: and | or ))/i).reject(&:empty?)

		puts "TERMS"
		puts terms

		pairs = terms.each_slice(2).map { |text, op| ["body LIKE ? #{op} ", "%#{text}%"] }

		puts "PAIRS"
		puts pairs

		query = pairs.reduce([""]) { |acc, terms| acc[0] += terms[0]; acc << terms[1] }

		puts "QUERY"
		puts query

		@tables = Document.where(query[0], *query[1..-1]).to_sql
		puts @tables
		@documents = ActiveRecord::Base.connection.execute(@tables)

		# if @documents.present?
		# 	return @documents
		# else
		# 	return nil
		# end
		 
		puts "Documents"
		puts @documents
		puts "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
		
    # @q = Document.ransack(params[:q])
    # @documents = @q.result(distinct: true)
  end

  # GET /documents/1 or /documents/1.json
  def show
  end

  # GET /documents/new
  def new
    @document = Document.new
  end

  # GET /documents/1/edit
  def edit
  end

  # POST /documents or /documents.json
  def create
    @document = Document.new(document_params)

    respond_to do |format|
      if @document.save
        format.html { redirect_to @document, notice: "Document was successfully created." }
        format.json { render :show, status: :created, location: @document }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @document.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /documents/1 or /documents/1.json
  def update
    respond_to do |format|
      if @document.update(document_params)
        format.html { redirect_to @document, notice: "Document was successfully updated." }
        format.json { render :show, status: :ok, location: @document }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @document.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /documents/1 or /documents/1.json
  def destroy
    @document.destroy
    respond_to do |format|
      format.html { redirect_to documents_url, notice: "Document was successfully destroyed." }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_document
      @document = Document.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def document_params
      params.require(:document).permit(:url, :title, :body, :search, :q, :title_or_body_cont, :m)
    end
end
