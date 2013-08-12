{
  'includes': [ '../common.gyp' ],
  'targets': [
    {
      'target_name': 'libtesseract',
      'type': 'static_library',
      'defines': [
        'LOCALEDIR', #TODO: set this to "$(localedir)" or not?
        'USE_STD_NAMESPACE',
      ],
      'dependencies': [
        '../leptonica/leptonica.gyp:liblept'
      ],
      'include_dirs': [
        '../leptonica/src',
        'api',
        'ccmain',
        'ccstruct',
        'ccutil',
        'classify',
        'cube',
        'cutil',
        'dict',
        'image',
        'neural_networks/runtime',
        'textord',
        'viewer',
        'wordrec',
      ],
      'sources': [
        'api/baseapi.cpp',
        'api/capi.cpp',
        #'api/tesseractmain.cpp',
        'ccmain/adaptions.cpp',
        'ccmain/applybox.cpp',
        'ccmain/control.cpp',
        'ccmain/cubeclassifier.cpp',
        'ccmain/cube_control.cpp',
        'ccmain/cube_reco_context.cpp',
        'ccmain/docqual.cpp',
        'ccmain/equationdetect.cpp',
        'ccmain/fixspace.cpp',
        'ccmain/fixxht.cpp',
        'ccmain/imgscale.cpp',
        'ccmain/ltrresultiterator.cpp',
        'ccmain/osdetect.cpp',
        'ccmain/output.cpp',
        'ccmain/pageiterator.cpp',
        'ccmain/pagesegmain.cpp',
        'ccmain/pagewalk.cpp',
        'ccmain/paragraphs.cpp',
        'ccmain/paramsd.cpp',
        'ccmain/pgedit.cpp',
        'ccmain/recogtraining.cpp',
        'ccmain/reject.cpp',
        'ccmain/resultiterator.cpp',
        'ccmain/scaleimg.cpp',
        'ccmain/tessbox.cpp',
        'ccmain/tessedit.cpp',
        'ccmain/tesseractclass.cpp',
        'ccmain/tesseract_cube_combiner.cpp',
        'ccmain/tessvars.cpp',
        'ccmain/tfacepp.cpp',
        'ccmain/thresholder.cpp',
        'ccmain/werdit.cpp',
        'ccstruct/blobbox.cpp',
        'ccstruct/blobs.cpp',
        'ccstruct/blread.cpp',
        'ccstruct/boxread.cpp',
        'ccstruct/boxword.cpp',
        'ccstruct/ccstruct.cpp',
        'ccstruct/coutln.cpp',
        'ccstruct/detlinefit.cpp',
        'ccstruct/dppoint.cpp',
        'ccstruct/fontinfo.cpp',
        'ccstruct/genblob.cpp',
        'ccstruct/linlsq.cpp',
        'ccstruct/matrix.cpp',
        'ccstruct/mod128.cpp',
        'ccstruct/normalis.cpp',
        'ccstruct/ocrblock.cpp',
        'ccstruct/ocrpara.cpp',
        'ccstruct/ocrrow.cpp',
        'ccstruct/otsuthr.cpp',
        'ccstruct/pageres.cpp',
        'ccstruct/pdblock.cpp',
        'ccstruct/points.cpp',
        'ccstruct/polyaprx.cpp',
        'ccstruct/polyblk.cpp',
        'ccstruct/publictypes.cpp',
        'ccstruct/quadlsq.cpp',
        'ccstruct/quadratc.cpp',
        'ccstruct/quspline.cpp',
        'ccstruct/ratngs.cpp',
        'ccstruct/rect.cpp',
        'ccstruct/rejctmap.cpp',
        'ccstruct/seam.cpp',
        'ccstruct/split.cpp',
        'ccstruct/statistc.cpp',
        'ccstruct/stepblob.cpp',
        'ccstruct/vecfuncs.cpp',
        'ccstruct/werd.cpp',
        'ccutil/ambigs.cpp',
        'ccutil/basedir.cpp',
        'ccutil/bits16.cpp',
        'ccutil/bitvector.cpp',
        'ccutil/ccutil.cpp',
        'ccutil/clst.cpp',
        'ccutil/elst.cpp',
        'ccutil/elst2.cpp',
        'ccutil/errcode.cpp',
        'ccutil/globaloc.cpp',
        'ccutil/hashfn.cpp',
        'ccutil/indexmapbidi.cpp',
        'ccutil/mainblk.cpp',
        'ccutil/memry.cpp',
        'ccutil/mfcpch.cpp',
        'ccutil/params.cpp',
        'ccutil/scanutils.cpp',
        'ccutil/serialis.cpp',
        'ccutil/strngs.cpp',
        'ccutil/tessdatamanager.cpp',
        'ccutil/tprintf.cpp',
        'ccutil/unichar.cpp',
        'ccutil/unicharmap.cpp',
        'ccutil/unicharset.cpp',
        'ccutil/unicodes.cpp',
        'classify/adaptive.cpp',
        'classify/adaptmatch.cpp',
        'classify/blobclass.cpp',
        'classify/chartoname.cpp',
        'classify/classify.cpp',
        'classify/cluster.cpp',
        'classify/clusttool.cpp',
        'classify/cutoffs.cpp',
        'classify/errorcounter.cpp',
        'classify/extract.cpp',
        'classify/featdefs.cpp',
        'classify/flexfx.cpp',
        'classify/float2int.cpp',
        'classify/fpoint.cpp',
        'classify/fxdefs.cpp',
        'classify/intfeaturedist.cpp',
        'classify/intfeaturemap.cpp',
        'classify/intfeaturespace.cpp',
        'classify/intfx.cpp',
        'classify/intmatcher.cpp',
        'classify/intproto.cpp',
        'classify/kdtree.cpp',
        'classify/mastertrainer.cpp',
        'classify/mf.cpp',
        'classify/mfdefs.cpp',
        'classify/mfoutline.cpp',
        'classify/mfx.cpp',
        'classify/normfeat.cpp',
        'classify/normmatch.cpp',
        'classify/ocrfeatures.cpp',
        'classify/outfeat.cpp',
        'classify/picofeat.cpp',
        'classify/protos.cpp',
        'classify/sampleiterator.cpp',
        'classify/shapetable.cpp',
        'classify/speckle.cpp',
        'classify/tessclassifier.cpp',
        'classify/trainingsample.cpp',
        'classify/trainingsampleset.cpp',
        'classify/xform2d.cpp',
        'cube/altlist.cpp',
        'cube/beam_search.cpp',
        'cube/bmp_8.cpp',
        'cube/cached_file.cpp',
        'cube/char_altlist.cpp',
        'cube/char_bigrams.cpp',
        'cube/char_samp.cpp',
        'cube/char_samp_enum.cpp',
        'cube/char_samp_set.cpp',
        'cube/char_set.cpp',
        'cube/classifier_factory.cpp',
        'cube/conv_net_classifier.cpp',
        'cube/con_comp.cpp',
        'cube/cube_line_object.cpp',
        'cube/cube_line_segmenter.cpp',
        'cube/cube_object.cpp',
        'cube/cube_search_object.cpp',
        'cube/cube_tuning_params.cpp',
        'cube/cube_utils.cpp',
        'cube/feature_bmp.cpp',
        'cube/feature_chebyshev.cpp',
        'cube/feature_hybrid.cpp',
        'cube/hybrid_neural_net_classifier.cpp',
        'cube/search_column.cpp',
        'cube/search_node.cpp',
        'cube/tess_lang_model.cpp',
        'cube/tess_lang_mod_edge.cpp',
        'cube/word_altlist.cpp',
        'cube/word_list_lang_model.cpp',
        'cube/word_size_model.cpp',
        'cube/word_unigrams.cpp',
        'cutil/bitvec.cpp',
        'cutil/callcpp.cpp',
        'cutil/cutil.cpp',
        'cutil/cutil_class.cpp',
        'cutil/danerror.cpp',
        'cutil/efio.cpp',
        'cutil/emalloc.cpp',
        'cutil/freelist.cpp',
        'cutil/listio.cpp',
        'cutil/oldheap.cpp',
        'cutil/oldlist.cpp',
        'cutil/structures.cpp',
        'cutil/tessarray.cpp',
        'dict/context.cpp',
        'dict/dawg.cpp',
        'dict/dict.cpp',
        'dict/hyphen.cpp',
        'dict/permdawg.cpp',
        'dict/permute.cpp',
        'dict/states.cpp',
        'dict/stopper.cpp',
        'dict/trie.cpp',
        'image/image.cpp',
        'image/imgs.cpp',
        'image/imgtiff.cpp',
        'image/svshowim.cpp',
        'neural_networks/runtime/input_file_buffer.cpp',
        'neural_networks/runtime/neural_net.cpp',
        'neural_networks/runtime/neuron.cpp',
        'neural_networks/runtime/sigmoid_table.cpp',
        'textord/alignedblob.cpp',
        'textord/bbgrid.cpp',
        'textord/blkocc.cpp',
        'textord/blobgrid.cpp',
        'textord/ccnontextdetect.cpp',
        'textord/cjkpitch.cpp',
        'textord/colfind.cpp',
        'textord/colpartition.cpp',
        'textord/colpartitiongrid.cpp',
        'textord/colpartitionset.cpp',
        'textord/devanagari_processing.cpp',
        'textord/drawedg.cpp',
        'textord/drawtord.cpp',
        'textord/edgblob.cpp',
        'textord/edgloop.cpp',
        'textord/equationdetectbase.cpp',
        'textord/fpchop.cpp',
        'textord/gap_map.cpp',
        'textord/imagefind.cpp',
        'textord/linefind.cpp',
        'textord/makerow.cpp',
        'textord/oldbasel.cpp',
        'textord/pithsync.cpp',
        'textord/pitsync1.cpp',
        'textord/scanedg.cpp',
        'textord/sortflts.cpp',
        'textord/strokewidth.cpp',
        'textord/tabfind.cpp',
        'textord/tablefind.cpp',
        'textord/tablerecog.cpp',
        'textord/tabvector.cpp',
        'textord/textlineprojection.cpp',
        'textord/textord.cpp',
        'textord/topitch.cpp',
        'textord/tordmain.cpp',
        'textord/tospace.cpp',
        'textord/tovars.cpp',
        'textord/underlin.cpp',
        'textord/wordseg.cpp',
        'textord/workingpartset.cpp',
        'viewer/scrollview.cpp',
        'viewer/svmnode.cpp',
        'viewer/svpaint.cpp',
        'viewer/svutil.cpp',
        'wordrec/associate.cpp',
        'wordrec/bestfirst.cpp',
        'wordrec/chop.cpp',
        'wordrec/chopper.cpp',
        'wordrec/closed.cpp',
        'wordrec/drawfx.cpp',
        'wordrec/findseam.cpp',
        'wordrec/gradechop.cpp',
        'wordrec/heuristic.cpp',
        'wordrec/language_model.cpp',
        'wordrec/makechop.cpp',
        'wordrec/matchtab.cpp',
        'wordrec/olutil.cpp',
        'wordrec/outlines.cpp',
        'wordrec/pieces.cpp',
        'wordrec/plotedges.cpp',
        'wordrec/plotseg.cpp',
        'wordrec/render.cpp',
        'wordrec/segsearch.cpp',
        'wordrec/tface.cpp',
        'wordrec/wordclass.cpp',
        'wordrec/wordrec.cpp',
      ],
      'conditions': [
        ['OS=="win"',
          {
            'defines': [
              '__MSW32__',
              '_CRT_SECURE_NO_WARNINGS',
              'WINDLLNAME="libtesseract"',
            ],
            'include_dirs': [
              'port',
            ],
            'sources': [
              'port/gettimeofday.cpp',
              'port/strtok_r.cpp',
            ],
            'link_settings': {
              'libraries': [
                '-lws2_32.lib',
                '-lUser32.lib',
              ],
            },
            'configurations': {
              'Debug': {
                'msvs_settings': {
                  'VCCLCompilerTool': {
                    'CompileAs': '2',
                  },
                },
              },
              'Release': {
                'msvs_settings': {
                  'VCCLCompilerTool': {
                    'CompileAs': '2',
                  },
                },
              },
            },
          }
        ]
      ]
    },
  ]
}
