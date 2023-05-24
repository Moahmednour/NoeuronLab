

from redact.types.pre_processing_bundle import PdfPreProcessingBundle
from redact.types.file_bundle import FileBundle


class TestPdfPreProcessingBundle:
    def test_from_file_bundle(self) -> None:
        intial_bundle = FileBundle(
            image_file_name="a.pdf",
            fott_file_name="a.pdf.labels.json",
            ocr_file_name="a.pdf.ocr.json")

        expected_rendered_file_name = "a.pdf.rendered.png"
        expected_corrected_ocr_file_name = "a.pdf.corrected.ocr.json"

        pdf_pundle = PdfPreProcessingBundle.from_file_bundle(intial_bundle)

        assert pdf_pundle.rendered_file_name == expected_rendered_file_name
        assert pdf_pundle.corrected_ocr_file_name == expected_corrected_ocr_file_name
