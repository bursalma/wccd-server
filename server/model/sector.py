from .base import BaseModel, db, now


class SectorConviction(db.Model, BaseModel):
    __tablename__ = 'sector_conviction'
    sector_id = db.Column(db.Integer, db.ForeignKey('sector.id'),
                          primary_key=True)
    conviction_id = db.Column(db.Integer, db.ForeignKey('conviction.id'),
                              primary_key=True)
    last_update = db.Column(db.DateTime, default=now, onupdate=now)


class Sector(db.Model, BaseModel):
    __tablename__ = 'sector'
    id = db.Column(db.Integer, primary_key=True)
    sector = db.Column(db.String(85))
    sector_desc = db.Column(db.String(85))
    last_update = db.Column(db.DateTime, default=now, onupdate=now)
    all_conviction = db.relationship("Conviction",
                                     secondary=SectorConviction.__table__,
                                     back_populates="all_sector")
