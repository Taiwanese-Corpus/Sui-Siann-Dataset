document.addEventListener('DOMContentLoaded', function(){
  fetch('/phiaua/khuan/1')
  .then(response => response.json())
  .then(data => {
    let lui_kiatko = data.suan;
    // lui_kiatko=[
    //   { id:1, miâ:'本調', siktsuí:'red',},
    //   { id:2, miâ:'規則變調', siktsuí:'green',},
    // ]

    let luimia = lui => lui.miâ;
    let luisik = lui => lui.siktsuí;
    let liuamia = lui => 'liua-' + lui.id;
    let cssmia = lui => 'lui-' + lui.id;
    let sik = lui => 'sik-' + lui.id;
    let liuatsua = lui_kiatko.map(lui => liuamia(lui)).join(' ')

    tinymce.init({
      selector: 'textarea.phiaua',

      menubar: false,  
      toolbar: 'undo redo | '  + liuatsua,
      valid_classes: lui_kiatko.map(lui => cssmia(lui)).join(' '),
      valid_styles: {'*': ''},
      setup: function (editor) {
        editor.ui.registry.addContextToolbar('textselection', {
          predicate: function (node) {
            return !editor.selection.isCollapsed();
          },
          items: liuatsua,
          position: 'selection',
          scope: 'node'
        });

        lui_kiatko.forEach(lui => {
          editor.ui.registry.addIcon(
            cssmia(lui),
            `<svg width="24" height="24" style="fill: ${luisik(lui)};"><path d="M17.5 11.4A9 9 0 0118 14c0 .5 0 1-.2 1.4 0 .4-.3.9-.5 1.3a6.2 6.2 0 01-3.7 3 5.7 5.7 0 01-3.2 0A5.9 5.9 0 017.6 18a6.2 6.2 0 01-1.4-2.6 6.7 6.7 0 010-2.8c0-.4.1-.9.3-1.3a13.6 13.6 0 012.3-4A20 20 0 0112 4a26.4 26.4 0 013.2 3.4 18.2 18.2 0 012.3 4zm-2 4.5c.4-.7.5-1.4.5-2a7.3 7.3 0 00-1-3.2c.2.6.2 1.2.2 1.9a4.5 4.5 0 01-1.3 3 5.3 5.3 0 01-2.3 1.5 4.9 4.9 0 01-2 .1 4.3 4.3 0 002.4.8 4 4 0 002-.6 4 4 0 001.5-1.5z" fill-rule="evenodd"></path></svg>`
          );
          editor.ui.registry.addToggleButton(liuamia(lui), {
            icon: cssmia(lui),
            text: luimia(lui),
            onAction: function (_) {
              
              editor.execCommand('RemoveFormat');
              editor.execCommand('FormatBlock', false, sik(lui));
            },
            onSetup: function (api) {
              editor.formatter.formatChanged(sik(lui), function (state) {
                api.setActive(state);
              });
            }
          })
        })
      },

      content_style: lui_kiatko.map(lui => `.${cssmia(lui)} \{ ${data.iunn}: ${luisik(lui)}; \}`).join(' '),
      // content_style: 
      //   '.lui-1 { color: green; } ' +
      //   '.lui-2 { color: red; } ',

      formats: Object.fromEntries(
        lui_kiatko.map(lui => [
          sik(lui), {classes: cssmia(lui), inline: 'span', exact: true}
        ])
      ),
      // formats: {
      //   'sik-1': { inline: 'span', classes: 'lui-1', exact: true },
      //   'sik-2': { inline: 'span', classes: 'lui-2', exact: true },
      // },

      style_formats: lui_kiatko.map(lui => (
        { title: luimia(lui), format: sik(lui) }
      )),
      // style_formats: [
      //   { title: '本調', format: 'sik-1' },
      //   { title: '變調', format: 'sik-2' },
      // ],
    });


  });
});