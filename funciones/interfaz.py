import libglade, gtk
from funciones import conversiones

class EuroConversor:
    def __init__(self):
        self.arbol = libglade.GladeXML( "uno.glade", "window1" )
        self.caja1 = self.arbol.get_widget( "entry1" )
        self.caja2 = self.arbol.get_widget( "entry2" )

        manejadores = { "on_entry1_key_press_event" : self.pasar,
                        "on_entry2_key_press_event" : self.pasar,
#                        "on_entry1_changed" : self.pasar,
#                        "on_entry2_changed" : self.pasar,
                       }
        self.arbol.signal_autoconnect( manejadores )
        self.arbol.signal_connect( "on_window1_destroy", self.salir )

    def a_correr(self):
        gtk.mainloop()

    def salir(self, obj):
        print "Saliendo..."
        gtk.mainquit()

    def pasar(self, obj, ev):
        """  En 'obj' viene el objeto que llama (la caja de texto),
             En 'ev' viene el evento, dir(ev) = keyval, send_event, state, string, time, type, window
        """
        nombre = libglade.get_widget_name( obj )
        if nombre == "entry1":
           entrada_validada1 = conversiones.validar_entrada1(obj.get_text() + ev.string)
           if entrada_validada1:
                self.caja2.set_text( conversiones.pelas_a_euros( entrada_validada1 ) )
           else:
                self.caja1.set_text( "" )
                self.caja2.set_text( "" )
        elif nombre == "entry2":
           entrada_validada2 = conversiones.validar_entrada2(obj.get_text() + ev.string)
           if entrada_validada2:
                self.caja1.set_text( conversiones.euros_a_pelas( entrada_validada2 ) )
           else:
                self.caja1.set_text( "" )
                self.caja2.set_text( "" )


