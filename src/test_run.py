# # from QuoteEngine import TextIngestor, PDFIngestor, CSVIngestor, DocxIngestor


# from PIL import Image

# from Ingestor import Ingestor

# from MemeGenerator import ImageCaptioner


# # print(DocxIngestor.parse("./_data/DogQuotes/DogQuotesDOCX.docx"))
# # print(CSVIngestor.parse("./_data/DogQuotes/DogQuotesCSV.csv"))
# # print(PDFIngestor.parse("./_data/DogQuotes/DogQuotesPDF.pdf"))
# # print(TextIngestor.parse("./_data/DogQuotes/DogQuotesTXT.txt"))
# file_paths = [
#     "./_data/DogQuotes/DogQuotesTXT.txt",
#     "./_data/DogQuotes/DogQuotesPDF.pdf",
#     "./_data/DogQuotes/DogQuotesCSV.csv",
#     # "./_data/DogQuotes/DogQuotesDOCX.docx",
# ]
# for file in file_paths:
#     result = Ingestor.parse(file)
#     print(result)
# captioner = ImageCaptioner("export_dir")


# print(
#     captioner.make_meme(
#         "./_data/photos/dog/xander_1.jpg", "this is monkey", "banur", 600
#     )
# )
