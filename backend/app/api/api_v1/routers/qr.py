from fastapi import APIRouter, Depends, HTTPException, Response
from io import BytesIO
import qrcode
from app.core.config import Settings, get_settings

router = APIRouter()


@router.get("/qr", summary="Generate a QR code")
async def generate_qr(
    data: str,
    settings: Settings = Depends(get_settings),
):
    """
    - **data**: text or URL to encode
    - Uses QR_SIZE, QR_BORDER, QR_FORMAT from settings
    """
    try:
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=settings.QR_SIZE // 100 or 3,
            border=settings.QR_BORDER,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        buf = BytesIO()
        img.save(buf, format=settings.QR_FORMAT)
        buf.seek(0)

        media_type = (
            "image/png"
            if settings.QR_FORMAT.upper() == "PNG"
            else "image/svg+xml"
        )
        return Response(buf.getvalue(), media_type=media_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
