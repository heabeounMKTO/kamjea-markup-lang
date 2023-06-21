use std::collections::HashMap;

pub struct KML_elem{
    html: String,
    kml: String,
}
impl KML_elem{
    pub fn new(&self, html: html, kml: kml) -> KML_elem{
        return KML_elem{html: html, kml: kml};
    }
    pub fn kml(&self) -> String{
        return self.kml;
    }

    pub fn html(&self) -> String{
        return self.html;
    }
}
